# Sources — Monotone NAE-3SAT Investigation

## Primary and canonical sources

- Thomas J. Schaefer, “The Complexity of Satisfiability Problems,” *STOC*, 1978 — Boolean satisfiability dichotomy; establishes hardness of the NAE relation outside the tractable Schaefer classes. https://doi.org/10.1145/800133.804350
- Andreas Darmann and Janosch Döcker, “On Simplified NP-Complete Variants of Not-All-Equal 3-SAT and 3-SAT,” 2019 — proves NP-completeness for Monotone NAE-3SAT under strong restrictions, including linear 4-regular instances. https://arxiv.org/abs/1908.04198
- Andreas Darmann and Janosch Döcker, “Planar NAE3SAT is in P,” 2019 — records the polynomial planar boundary. https://arxiv.org/abs/1904.07825
- Stefan Porschen, Dieter Randerath, and Ewald Speckenmeyer, “Linear Time Algorithms for Some Not-All-Equal Satisfiability Problems,” *SAT 2003* — includes polynomial algorithms for bounded-occurrence NAE variants and is cited by the restricted-hardness literature for the occurrence-at-most-three boundary. https://doi.org/10.1007/978-3-540-24605-3_18

## Use restrictions

- General NP-completeness does not imply that every restricted family is hard.
- Linear 4-regular hardness is a robustness control, not a claim about all linear or all regular subclasses.
- Planarity and bounded occurrence are tractable boundaries that every universal mechanism must classify correctly.
- Literature results are `ESTABLISHED`; only proofs written in this investigation receive project status `PROVED`.
