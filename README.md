# research-copilot

English | [中文](README.cn.md) · [Research Skillbox](https://github.com/windyvictor/research-skillbox)

A rigorous research collaboration skill for mathematics, optimization, machine learning, related theory, algorithms, computational experiments, empirical design, novelty analysis, and research workflow planning.

## Why this skill

Research problems rarely fit a single prompt. A proof depends on hidden assumptions; a novelty claim depends on component-level literature; an experiment can run while implementing the wrong method; a reproduced table may still use leaked data. This skill treats each of these as a different verification problem.

### What you get

- Proofs and derivations with definitions, domains, dimensions, boundary cases, and missing conditions exposed
- Novelty maps that compare mechanisms and formulas rather than keyword combinations
- Experiment plans with baselines, ablations, leakage checks, metrics, and stopping conditions
- Reproduction records that distinguish code execution, implementation fidelity, and result agreement
- A cross-stage research plan only when the task genuinely spans several stages

**Workflow:** classify the research task → expose assumptions → choose the required proof, search, computation, or experiment → execute → verify the observable result.

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

