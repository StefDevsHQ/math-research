from __future__ import annotations

import itertools
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from nae3sat import (
    EdgeDeletionCertificate,
    ValidationError,
    VertexDeletionCertificate,
    all_ordering_profile_aggregate,
    complete_three_graph,
    delete_edge,
    delete_vertex,
    edge_deletion_certificates,
    fano_plane,
    is_edge_minimal_unsatisfiable,
    is_vertex_minimal_unsatisfiable,
    labelled_instances,
    obstruction_atlas_bytes,
    obstruction_atlas_record,
    solve_exact,
    verify_coloring,
    verify_obstruction_atlas_record,
    vertex_deletion_certificates,
)

ROOT = Path(__file__).parents[1]
ATLAS = ROOT / "obstruction-atlas" / "vs05-obstruction-atlas.json"


def _reference_solutions(instance):
    return tuple(
        assignment
        for assignment in itertools.product((0, 1), repeat=instance.n)
        if all(not (assignment[a] == assignment[b] == assignment[c]) for a, b, c in instance.edges)
    )


def _reference_edge_minimal(instance):
    if _reference_solutions(instance):
        return False
    for edge in instance.edges:
        reduced_edges = tuple(value for value in instance.edges if value != edge)
        if not _reference_solutions(type(instance)(instance.n, reduced_edges)):
            return False
    return True


def _reference_vertex_minimal(instance):
    if _reference_solutions(instance):
        return False
    for vertex in range(instance.n):
        reduced = delete_vertex(instance, vertex).graph
        if not _reference_solutions(reduced):
            return False
    return True


class ObstructionPrimitiveTests(unittest.TestCase):
    def test_named_instances_and_strict_deletions(self):
        complete = complete_three_graph(5)
        self.assertEqual(len(complete.edges), 10)
        self.assertEqual(len(fano_plane().edges), 7)
        with self.assertRaises(ValidationError):
            complete_three_graph(True)
        with self.assertRaises(ValidationError):
            delete_edge(complete, (0, 1, 9))
        with self.assertRaises(ValidationError):
            delete_vertex(complete, True)

    def test_certificate_constructor_validation(self):
        EdgeDeletionCertificate((0, 1, 2), (0, 1, 0))
        VertexDeletionCertificate(2, (0, 1, 3), (0, 1, 0))
        with self.assertRaises(ValidationError):
            EdgeDeletionCertificate((0, 0, 1), (0, 1))
        with self.assertRaises(ValidationError):
            VertexDeletionCertificate(2, (0, 2), (0, 1))

    def test_complete_small_domain(self):
        totals = [1, 1, 1, 2, 16, 1024]
        expected_unsat = [0, 0, 0, 0, 0, 1]
        for n in range(6):
            count = unsat = edge_minimal = vertex_minimal = 0
            for instance in labelled_instances(n):
                reference = _reference_solutions(instance)
                result = solve_exact(instance)
                self.assertEqual(result.satisfiable, bool(reference))
                if result.witness is not None:
                    self.assertEqual(result.witness, reference[0])
                count += 1
                if reference:
                    continue
                unsat += 1
                reference_edge = _reference_edge_minimal(instance)
                reference_vertex = _reference_vertex_minimal(instance)
                self.assertEqual(is_edge_minimal_unsatisfiable(instance), reference_edge)
                self.assertEqual(is_vertex_minimal_unsatisfiable(instance), reference_vertex)
                edge_minimal += reference_edge
                vertex_minimal += reference_vertex
            self.assertEqual(count, totals[n])
            self.assertEqual((unsat, edge_minimal, vertex_minimal), (expected_unsat[n],) * 3)


class NamedObstructionTests(unittest.TestCase):
    def _check_obstruction(self, instance):
        self.assertFalse(_reference_solutions(instance))
        self.assertTrue(is_edge_minimal_unsatisfiable(instance))
        self.assertTrue(is_vertex_minimal_unsatisfiable(instance))

        edge_certificates = edge_deletion_certificates(instance)
        self.assertEqual(tuple(certificate.edge for certificate in edge_certificates), instance.edges)
        for certificate in edge_certificates:
            reduced = delete_edge(instance, certificate.edge)
            reference = _reference_solutions(reduced)
            self.assertTrue(reference)
            self.assertEqual(certificate.witness, reference[0])
            self.assertTrue(verify_coloring(reduced, certificate.witness))

        vertex_certificates = vertex_deletion_certificates(instance)
        self.assertEqual(tuple(certificate.vertex for certificate in vertex_certificates), tuple(range(instance.n)))
        for certificate in vertex_certificates:
            reduced = delete_vertex(instance, certificate.vertex)
            self.assertEqual(certificate.new_to_old, reduced.new_to_old)
            reference = _reference_solutions(reduced.graph)
            self.assertTrue(reference)
            self.assertEqual(certificate.witness, reference[0])
            self.assertTrue(verify_coloring(reduced.graph, certificate.witness))

    def test_complete_five_certificates(self):
        instance = complete_three_graph(5)
        self._check_obstruction(instance)
        degrees = [0] * instance.n
        codegrees = {(a, b): 0 for a, b in itertools.combinations(range(instance.n), 2)}
        for edge in instance.edges:
            for vertex in edge:
                degrees[vertex] += 1
            for pair in itertools.combinations(edge, 2):
                codegrees[pair] += 1
        self.assertEqual(degrees, [6] * 5)
        self.assertEqual(set(codegrees.values()), {3})

    def test_fano_certificates(self):
        instance = fano_plane()
        self._check_obstruction(instance)
        degrees = [0] * instance.n
        codegrees = {(a, b): 0 for a, b in itertools.combinations(range(instance.n), 2)}
        for edge in instance.edges:
            for vertex in edge:
                degrees[vertex] += 1
            for pair in itertools.combinations(edge, 2):
                codegrees[pair] += 1
        self.assertEqual(degrees, [3] * 7)
        self.assertEqual(set(codegrees.values()), {1})

    def test_all_ordering_profile_counts(self):
        complete = all_ordering_profile_aggregate(complete_three_graph(5))
        fano = all_ordering_profile_aggregate(fano_plane())
        self.assertEqual(complete["ordering_count"], 120)
        self.assertEqual(fano["ordering_count"], 5040)
        self.assertEqual(sum(complete["max_classes"]["distribution"].values()), 120)
        self.assertEqual(sum(fano["max_classes"]["distribution"].values()), 5040)
        self.assertEqual(len(complete["profile_sequence_sha256"]), 64)
        self.assertEqual(len(fano["profile_sequence_sha256"]), 64)


@unittest.skipUnless(os.environ.get("NAE3_FULL_VS05_ATLAS") == "1", "full atlas gate runs once in CI")
class AtlasRecordTests(unittest.TestCase):
    def test_record_and_committed_bytes(self):
        record = obstruction_atlas_record()
        self.assertTrue(verify_obstruction_atlas_record(record))
        totals = record["small_domain_census"]["totals"]
        self.assertEqual(totals, {
            "instances": 1045,
            "unsatisfiable": 1,
            "edge_minimal_unsatisfiable": 1,
            "vertex_minimal_unsatisfiable": 1,
            "both_minimal": 1,
        })
        self.assertEqual([item["name"] for item in record["named_obstructions"]], ["complete-three-graph-five", "fano-plane"])
        self.assertEqual(ATLAS.read_bytes(), obstruction_atlas_bytes())

    def test_cli_reproduction(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "atlas.json"
            run = subprocess.run(
                [sys.executable, "-m", "nae3sat.cli", "obstruction-atlas", "--output", str(output)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(output.read_bytes(), obstruction_atlas_bytes())
            self.assertTrue(verify_obstruction_atlas_record(json.loads(output.read_text())))


if __name__ == "__main__":
    unittest.main()
