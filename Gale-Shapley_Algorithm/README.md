# Gale-Shapley Algorithm

## Introduction
The Gale-Shapley algorithm, also known as the Stable Marriage algorithm, is a mathematical algorithm for solving the stable matching problem. It was devised by David Gale and Lloyd Shapley in 1962 and has applications in various fields, including economics, computer science, and game theory.

## Problem Statement
Given $n$ men and $n$ women, where each person has ranked all members of the opposite sex in order of preference, the goal is to find a stable matching where no two individuals would prefer each other over their current partners.

## Algorithm Overview
The Gale-Shapley algorithm works as follows:

1. Each man proposes to his most preferred woman who has not yet rejected him.
2. Each woman receives proposals from men and accepts the proposal from her most preferred man.
3. If a woman receives multiple proposals, she rejects all but the most preferred one.
4. If a man's proposal is rejected, he proposes to his next most preferred woman.
5. This process continues until each man is matched with a woman.

The resulting matching is guaranteed to be stable, meaning there are no two individuals who would both prefer each other over their current partners.

## Explanation
Let's denote:
- \$(M\)$ as the set of men.
- \$(W\)$ as the set of women.
- \$(m\)$ as a particular man.
- \$(w\)$ as a particular woman.
- \$(p\)$ as the preference list of a person.

Each person has a preference list \$(p\)$ ranking members of the opposite sex. For example, \$(p_m(w)\)$ represents the rank of woman \$(w\)$ on man \$(m\)$'s preference list.

A matching is a set of pairs \$(m, w\)$ where \$(m\)$ is a man, \$(w\)$ is a woman, and each person is matched with at most one person from the opposite sex.

A matching is stable if there are no two pairs \$(m_1, w_1\)$ and \$(m_2, w_2\)$ such that:
1. \$(m_1\)$ prefers \$(w_2\)$ over \$(w_1\)$ and \$(w_2\)$ prefers \$(m_1\)$ over \$(m_2\)$.
2. \$(w_1\)$ prefers \$(m_2\)$ over \$(m_1\)$ and \$(m_2\)$ prefers \$(w_1\)$ over \$(w_2\)$.

The Gale-Shapley algorithm produces a stable matching by ensuring that each man proposes to his most preferred woman who has not yet rejected him, and each woman accepts the proposal of her most preferred man. If a woman receives multiple proposals, she chooses the most preferred one and rejects all others.

## Example
For example, consider the following preference lists:

Men preferences:
- \$(m_1: [w_1, w_2, w_3]\)$
- \$(m_2: [w_2, w_1, w_3]\)$
- \$(m_3: [w_1, w_3, w_2]\)$

Women preferences:
- \$(w_1: [m_2, m_1, m_3]\)$
- \$(w_2: [m_1, m_2, m_3]\)$
- \$(w_3: [m_3, m_2, m_1]\)$

The Gale-Shapley algorithm would produce a stable matching where each man is matched with a woman such that no two individuals would prefer each other over their current partners.

