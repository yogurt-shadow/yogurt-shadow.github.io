---
title: Research Update - SMT Solving
date: 2025-09-28 11:00:00
tags: [research, SMT, formal methods]
categories: [Research]
img: https://yogurt-shadow.github.io/blog/images/image.png
---

# Research Update: Improving NLSAT for Nonlinear Real Arithmetic

## Overview

My recent work focuses on improving NLSAT (Nonlinear Real Arithmetic) solving techniques, particularly in the context of SMT solving.

![Research Image](https://yogurt-shadow.github.io/blog/images/image.png)

## Key Contributions

1. **Clause-level Decision Strategies**: Developed new strategies for NLSAT that improve solver efficiency on SMT-LIB benchmarks.

2. **Local Search Optimization**: Implemented efficient local search algorithms for nonlinear real arithmetic problems.

3. **Benchmark Performance**: Achieved significant improvements on standard SMT-LIB benchmarks.

## Technical Details

The main algorithmic improvements include:

- Enhanced clause selection heuristics
- Improved conflict analysis
- Better handling of nonlinear constraints

## Results

Our approach shows consistent improvements across multiple benchmark categories, particularly in:

- QF_NRA (Quantifier-Free Nonlinear Real Arithmetic)
- QF_LRA (Quantifier-Free Linear Real Arithmetic)

## Future Work

- Integration with existing SMT solvers
- Extension to other arithmetic domains
- Performance optimization for large-scale problems
