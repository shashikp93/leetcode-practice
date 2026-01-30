# Two Sum

## Problem Statement
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume:
- Exactly one solution exists
- Same element cannot be used twice

---

## Example
Input:
nums = [2,7,11,15]
target = 9
Output:
[0,1]

## Approach
We use a hashmap (dictionary) to store values and their indices.

For each number:
- Calculate complement = target - current number
- If complement exists in hashmap → return indices
- Otherwise store current number

