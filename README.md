# research-copilot

English | [中文](README.cn.md)

A rigorous research collaboration skill for mathematics, optimization, machine learning, related theory, algorithms, computational experiments, empirical design, novelty analysis, and research workflow planning.

## Use it for

- Proofs and derivations
- Assumption, boundary, and counterexample checks
- Research design and structural novelty analysis
- Algorithm implementation and numerical experiments
- Baseline reproduction, ablation, and data-leakage audits
- Empirical and qualitative research design
- Scientific writing checks when argument and evidence matter

## Contents

- `SKILL.md`: task classification and general research workflow
- `references/mathematical-proof.md`: proofs and derivations
- `references/novelty-analysis.md`: component and mechanism comparison
- `references/research-design.md`: problem and method design
- `references/algorithm-experiment.md`: algorithm and experiment analysis
- `references/ai-experiment-workflow.md`: implementation, execution, and reproducibility
- `references/empirical-research-design.md`: empirical methods
- `scripts/`: controlled-writing checkers
- `tests/`: checker regression tests
- `evals/`: behavioral cases

## Core rule

A claim is only as strong as its proof, data, computation, or verified source. Distinguish code that runs, an implementation that matches the target method, and results that reproduce a reported claim. “Not found” is not “does not exist.”

## Quick check

```bash
python3 scripts/check_controlled_writing.py manuscript.md
python3 -m unittest discover -s tests -v
```

## Install

```bash
git clone https://github.com/windyvictor/research-copilot.git
ln -s "$PWD/research-copilot" ~/.agents/skills/research-copilot
```

## License

MIT. Third-party standards, papers, and quoted materials retain their original rights.

