# Sources — Monotone NAE-3SAT Investigation

## Primary and canonical sources

- Thomas J. Schaefer, “The Complexity of Satisfiability Problems,” *STOC*, 1978 — Boolean satisfiability dichotomy; establishes hardness of the NAE relation outside the tractable Schaefer classes. https://doi.org/10.1145/800133.804350
- Andreas Darmann and Janosch Döcker, “On Simplified NP-Complete Variants of Not-All-Equal 3-SAT and 3-SAT,” 2019 — proves NP-completeness for Monotone NAE-3SAT under strong restrictions, including linear 4-regular instances. https://arxiv.org/abs/1908.04198
- Bernard M. E. Moret, “Planar NAE3SAT is in P,” *ACM SIGACT News* 19(2):51–54, 1988 — establishes the polynomial planar-incidence boundary through a planarity-preserving reduction to planar Simple MaxCut. https://doi.org/10.1145/49097.49099
- Stefan Porschen, Bert Randerath, and Ewald Speckenmeyer, “Linear Time Algorithms for Some Not-All-Equal Satisfiability Problems,” *SAT 2003*, LNCS 2919:172–187 — gives linear-time algorithms for restricted NAE classes and supports the occurrence-at-most-three tractability boundary used here. https://doi.org/10.1007/978-3-540-24605-3_14
- Yury Person and Mathias Schacht, “Almost all hypergraphs without Fano planes are bipartite,” *SODA 2009*, pp. 217–226 — records the Fano plane as the unique seven-vertex, seven-edge triple system with pair codegree one, non-two-colourable but two-colourable after every edge deletion. https://doi.org/10.1137/1.9781611973068.25

## Use restrictions

- General NP-completeness does not imply that every restricted family is hard.
- Linear 4-regular hardness is a robustness control, not a claim about all linear or all regular subclasses.
- Planarity and bounded occurrence are tractable boundaries that every universal mechanism must classify correctly.
- The Fano citation establishes a named sparse obstruction; it is not an exhaustive classification of seven-vertex obstructions.
- Literature results are `ESTABLISHED`; only proofs written in this investigation receive project status `PROVED`.
