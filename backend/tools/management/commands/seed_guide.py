from django.core.management.base import BaseCommand

from tools.models import Tool, GuidePattern, GuideExampleProblem

PATTERNS = [
    {
        "name": "Two Pointers",
        "how_it_works": (
            "Use two indices that move through a data structure (usually a sorted array or "
            "string) — either toward each other, or one chasing the other — to avoid nested loops."
        ),
        "recognition_signals": [
            "The input is a sorted array or can be sorted without losing needed info.",
            "You need to find a pair, triplet, or condition involving two elements.",
            "Keywords: \"pair that sums to,\" \"palindrome,\" \"sorted array,\" \"remove duplicates in place.\"",
        ],
        "code_solution": '''def two_sum_sorted(nums, target):
    # Because the array is sorted, we can reason about direction:
    # if the sum is too small, only moving 'left' rightward can increase it;
    # if too large, only moving 'right' leftward can decrease it.
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            # Found the exact pair — no need to search further.
            return [left, right]
        elif s < target:
            # Sum too small: the only way to increase it is to take a bigger
            # left value, so advance the left pointer.
            left += 1
        else:
            # Sum too large: the only way to decrease it is to take a smaller
            # right value, so pull the right pointer back.
            right -= 1

    return []  # No pair found
''',
        "example_problems": [
            {"title": "Two Sum II - Input Array Is Sorted", "description": "pointers start at both ends, move based on whether the sum is too high or too low."},
            {"title": "3Sum", "description": "fix one element, two-pointer the rest."},
            {"title": "Container With Most Water", "description": "move the pointer at the shorter line inward."},
            {"title": "Valid Palindrome", "description": "compare from outside in."},
        ],
    },
    {
        "name": "Sliding Window",
        "how_it_works": (
            "Maintain a \"window\" (subarray/substring) defined by two pointers, expanding and "
            "shrinking it as you scan, instead of recomputing from scratch for every subrange. "
            "Two variants: a fixed-size window, where the window size is given, and a "
            "variable-size window, where the window grows/shrinks based on a condition."
        ),
        "recognition_signals": [
            "Asked for a contiguous subarray/substring satisfying some condition.",
            "Keywords: \"longest/shortest substring,\" \"maximum sum subarray of size k,\" \"at most k distinct characters.\"",
        ],
        "code_solution": '''def longest_unique_substring(s):
    # seen[char] = the most recent index where char appeared.
    # This lets us jump 'left' directly instead of shrinking one step at a time.
    seen = {}
    left = max_len = 0

    for right, char in enumerate(s):
        # If char is already in our current window (its last index is >= left),
        # the window must shrink past that duplicate to stay valid.
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        # Record/update the last seen position of this character.
        seen[char] = right

        # The window [left, right] is now guaranteed duplicate-free;
        # check if it's the longest one seen so far.
        max_len = max(max_len, right - left + 1)

    return max_len
''',
        "example_problems": [
            {"title": "Best Time to Buy and Sell Stock", "description": "implicit sliding window tracking min so far."},
            {"title": "Longest Substring Without Repeating Characters", "description": "variable window with a set/map tracking seen characters."},
            {"title": "Minimum Window Substring", "description": "variable window with a frequency counter."},
            {"title": "Maximum Sum Subarray of Size K", "description": "fixed window."},
        ],
    },
    {
        "name": "Fast & Slow Pointers",
        "how_it_works": (
            "Two pointers move through a sequence (often a linked list) at different speeds. "
            "Useful for cycle detection and finding midpoints without extra space."
        ),
        "recognition_signals": [
            "Involves a linked list.",
            "Keywords: \"cycle,\" \"middle of the list,\" \"happy number,\" \"duplicate number in an array\" (treated as an implicit linked list).",
        ],
        "code_solution": '''def has_cycle(head):
    # slow moves 1 node per step, fast moves 2 nodes per step.
    # If there's no cycle, fast reaches the end (None) first, and we return False.
    # If there IS a cycle, fast will eventually "lap" slow inside the loop,
    # because the gap between them shrinks by 1 every step.
    slow = fast = head

    while fast and fast.next:
        slow = slow.next          # advance by 1
        fast = fast.next.next     # advance by 2
        if slow == fast:
            # They collided inside the cycle — a cycle must exist.
            return True

    return False  # fast hit the end of the list, so no cycle
''',
        "example_problems": [
            {"title": "Linked List Cycle", "description": "fast pointer moves 2 steps, slow moves 1; if they meet, there's a cycle."},
            {"title": "Middle of the Linked List", "description": "when fast reaches the end, slow is at the middle."},
            {"title": "Happy Number", "description": "detect a cycle in the sequence of digit-square sums."},
            {"title": "Find the Duplicate Number", "description": "Floyd's cycle detection on array-as-linked-list."},
        ],
    },
    {
        "name": "Merge Intervals",
        "how_it_works": (
            "Sort intervals by start time, then sweep through, merging overlapping ones or "
            "checking for conflicts."
        ),
        "recognition_signals": [
            "Input is a list of [start, end] ranges.",
            "Keywords: \"overlapping intervals,\" \"meeting rooms,\" \"insert interval,\" \"free time.\"",
        ],
        "code_solution": '''def merge(intervals):
    # Sorting by start time guarantees that any interval that could overlap
    # with our current merged interval will appear next in the scan —
    # we never need to look backward.
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        # If this interval's start is within the last merged interval's range,
        # they overlap (or touch), so extend the end if needed.
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            # No overlap with the last merged interval — start a new one.
            result.append([start, end])

    return result
''',
        "example_problems": [
            {"title": "Merge Intervals", "description": "sort, then merge if current.start <= previous.end."},
            {"title": "Insert Interval", "description": "merge a new interval into an already-sorted list."},
            {"title": "Meeting Rooms II", "description": "track overlap count, often with a min-heap of end times."},
        ],
    },
    {
        "name": "Binary Search",
        "how_it_works": (
            "Repeatedly halve the search space. The classic version searches a sorted array; "
            "the advanced version searches over a range of possible answers, checking "
            "feasibility at each midpoint."
        ),
        "recognition_signals": [
            "Sorted array, and you need better than O(n).",
            "Keywords: \"sorted,\" \"rotated sorted array,\" \"find minimum/maximum such that condition holds,\" \"search space.\"",
            "If a problem asks to minimize/maximize a value subject to a feasibility check that's "
            "monotonic (true, true, ..., false, false or vice versa), it's binary-search-the-answer.",
        ],
        "code_solution": '''def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        # Check the middle of the CURRENT search space, not the whole array —
        # this is what keeps each iteration O(1) and the total search O(log n).
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Target must be to the right: everything at or left of mid
            # is too small and can be discarded.
            left = mid + 1
        else:
            # Target must be to the left: everything at or right of mid
            # is too large and can be discarded.
            right = mid - 1

    return -1  # Search space is empty — target isn't present
''',
        "example_problems": [
            {"title": "Binary Search", "description": "the textbook version."},
            {"title": "Search in Rotated Sorted Array", "description": "modified binary search that figures out which half is sorted."},
            {"title": "Find Minimum in Rotated Sorted Array", "description": "same rotated-array reasoning, applied to finding the pivot."},
            {"title": "Koko Eating Bananas", "description": "binary search over possible \"eating speeds,\" checking feasibility with a helper function."},
            {"title": "Capacity To Ship Packages Within D Days", "description": "same pattern."},
        ],
    },
    {
        "name": "BFS on Trees & Graphs",
        "how_it_works": (
            "Breadth-first search explores a tree or graph level by level using a queue: visit a "
            "node, then enqueue all its unvisited neighbors, and repeat. Because it expands "
            "outward in \"rings\" from the start node, the first time BFS reaches a node is "
            "guaranteed to be via the shortest path (in an unweighted graph)."
        ),
        "recognition_signals": [
            "Keywords: \"shortest path,\" \"fewest steps,\" \"minimum number of moves,\" \"level order,\" \"nearest.\"",
            "Any time you need the minimum distance/steps between two nodes in an unweighted graph or grid.",
        ],
        "code_solution": '''from collections import deque

def num_islands_bfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def bfs(r, c):
        # A queue gives FIFO order, which is what makes this breadth-first:
        # we fully process all cells at the current "distance" before
        # moving on to cells one step farther away.
        queue = deque([(r, c)])
        visited.add((r, c))

        while queue:
            row, col = queue.popleft()  # dequeue the oldest cell added
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                # Only enqueue neighbors that are in bounds, part of land,
                # and not already queued/visited (avoids revisiting).
                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == '1' and (nr, nc) not in visited):
                    visited.add((nr, nc))  # mark visited the moment we enqueue
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            # Every time we find an unvisited land cell, it must belong to
            # a new island (BFS from earlier islands couldn't have reached it).
            if grid[r][c] == '1' and (r, c) not in visited:
                visited.add((r, c))
                bfs(r, c)
                count += 1

    return count
''',
        "example_problems": [
            {"title": "Binary Tree Level Order Traversal", "description": "BFS with a queue, tracking level boundaries."},
            {"title": "Word Ladder", "description": "BFS for the shortest transformation sequence between two words."},
            {"title": "Rotting Oranges", "description": "multi-source BFS spreading outward from all initially rotten oranges simultaneously."},
            {"title": "01 Matrix", "description": "BFS from all zero cells at once to find distance to nearest zero."},
        ],
    },
    {
        "name": "DFS on Trees & Graphs",
        "how_it_works": (
            "Depth-first search explores as far as possible down one path before backtracking, "
            "using recursion (the call stack) or an explicit stack. It's naturally suited to "
            "exploring all paths, checking connectivity, and problems with a recursive "
            "tree/graph structure.\n\n"
            "BFS vs. DFS at a glance: BFS uses a queue (FIFO) and explores level by level, "
            "outward — it's best for shortest path / minimum steps problems, and its space use "
            "can hold an entire \"level\" at once. DFS uses a stack or recursion (LIFO) and "
            "explores one path fully before backtracking — it's best for connectivity, all "
            "paths, and backtracking-style problems, and its space use is proportional to the "
            "depth of the recursion."
        ),
        "recognition_signals": [
            "Keywords: \"connected components,\" \"islands,\" \"all paths,\" \"path sum,\" \"validate tree structure,\" \"does a path exist.\"",
            "When the problem doesn't care about shortest distance, just about reachability, "
            "structure, or enumerating paths — DFS is usually simpler to write than BFS.",
        ],
        "code_solution": '''def num_islands_dfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        # Base case: stop recursing the moment we go out of bounds,
        # hit water, or hit a cell we've already claimed for this island.
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] != '1' or (r, c) in visited):
            return

        # Claim this cell as part of the current island before recursing,
        # so we never process it twice (prevents infinite recursion on cycles).
        visited.add((r, c))

        # Recurse in all 4 directions — the call stack itself tracks
        # "how far we've traveled," which is what makes this depth-first.
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                # Each fresh unvisited land cell is the seed of a new island;
                # dfs() below will consume every cell connected to it.
                dfs(r, c)
                count += 1

    return count
''',
        "example_problems": [
            {"title": "Number of Islands", "description": "DFS flood-fill marks an entire connected landmass at once."},
            {"title": "Path Sum", "description": "DFS down each root-to-leaf path, checking if any sums to the target."},
            {"title": "Course Schedule", "description": "DFS with a \"currently visiting\" set to detect cycles in a directed graph."},
            {"title": "Clone Graph", "description": "DFS with a hash map from original node to cloned node to avoid infinite recursion."},
        ],
    },
    {
        "name": "Dynamic Programming (DP)",
        "how_it_works": (
            "Break a problem into overlapping subproblems, solve each once, and store the "
            "result (memoization or tabulation) to avoid recomputation. The hardest part is "
            "finding the recurrence relation. Common sub-patterns: 1D DP (climbing stairs, "
            "house robber), 2D DP / grid DP (unique paths, edit distance), knapsack-style DP "
            "(subset sum, coin change), and DP on strings (longest common subsequence, "
            "palindromic substrings)."
        ),
        "recognition_signals": [
            "Problem asks for an optimal value (min/max/count of ways), and naive recursion would revisit the same subproblems.",
            "Keywords: \"number of ways,\" \"minimum cost/steps,\" \"maximum profit,\" \"longest,\" \"can you reach/partition.\"",
            "Test: does the brute-force recursive solution have overlapping calls? If yes, it's a DP candidate.",
        ],
        "code_solution": '''def coin_change(coins, amount):
    # dp[a] = fewest coins needed to make amount 'a'.
    # Initialize to "infinity" since we haven't found a way to make
    # most amounts yet; dp[0] = 0 because zero coins make amount 0.
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                # If we use this coin, the remaining amount is (a - coin),
                # which we've already solved optimally (bottom-up order
                # guarantees dp[a - coin] is finalized before dp[a]).
                # +1 accounts for the coin we just used.
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
''',
        "example_problems": [
            {"title": "Climbing Stairs", "description": "dp[i] = dp[i-1] + dp[i-2], Fibonacci-like."},
            {"title": "House Robber", "description": "dp[i] = max(dp[i-1], dp[i-2] + nums[i])."},
            {"title": "Coin Change", "description": "minimum coins to reach an amount, unbounded knapsack."},
            {"title": "Longest Common Subsequence", "description": "2D table comparing two strings."},
            {"title": "Edit Distance", "description": "2D DP with insert/delete/replace transitions."},
        ],
    },
    {
        "name": "Greedy Algorithms",
        "how_it_works": (
            "Make the locally optimal choice at each step, trusting that it leads to a globally "
            "optimal solution. Requires proving (or trusting) the greedy-choice property — not "
            "every problem allows this."
        ),
        "recognition_signals": [
            "Asked to minimize/maximize something, and sorting or a simple local rule seems to naturally lead to the answer.",
            "Keywords: \"minimum number of,\" \"maximum number of,\" \"intervals,\" \"jump game,\" \"assign.\"",
            "Red flag it's NOT greedy: if a locally good choice can lock you out of a better global solution (that's usually a DP problem instead).",
        ],
        "code_solution": '''def can_jump(nums):
    # 'farthest' greedily tracks the furthest index reachable so far,
    # using ONLY information seen up to the current position — we never
    # need to reconsider earlier decisions.
    farthest = 0

    for i, n in enumerate(nums):
        # If we can't even reach index i with our best reach so far,
        # no later index can help — we're stuck.
        if i > farthest:
            return False

        # Greedy update: from index i, jumping n steps could extend
        # our farthest reach. We only keep it if it's an improvement.
        farthest = max(farthest, i + n)

    return True
''',
        "example_problems": [
            {"title": "Jump Game", "description": "greedily track the farthest reachable index."},
            {"title": "Gas Station", "description": "greedily reset the starting point when the running total goes negative."},
            {"title": "Non-overlapping Intervals", "description": "sort by end time, greedily keep intervals that don't overlap."},
            {"title": "Task Scheduler", "description": "greedily schedule the most frequent task first."},
        ],
    },
    {
        "name": "Heap / Priority Queue",
        "how_it_works": (
            "Maintain a data structure that gives O(log n) access to the min or max element. "
            "Useful whenever you repeatedly need \"the smallest/largest remaining item.\""
        ),
        "recognition_signals": [
            "Keywords: \"kth largest/smallest,\" \"top k,\" \"merge k sorted lists,\" \"median of a stream,\" \"scheduling.\"",
        ],
        "code_solution": '''import heapq

def kth_largest(nums, k):
    # Strategy: keep a MIN-heap of size k containing the k largest
    # numbers seen so far. The smallest of those k (the heap's root)
    # is therefore the kth largest overall.
    heap = nums[:k]
    heapq.heapify(heap)  # O(k) to build the initial heap

    for n in nums[k:]:
        # If n is bigger than the smallest of our current "top k",
        # n belongs in the top k instead — swap it in.
        if n > heap[0]:
            heapq.heapreplace(heap, n)  # pop smallest, push n, O(log k)
        # Otherwise n definitely isn't in the top k; skip it entirely.

    # After processing everything, the root is exactly the kth largest.
    return heap[0]
''',
        "example_problems": [
            {"title": "Kth Largest Element in an Array", "description": "min-heap of size k."},
            {"title": "Top K Frequent Elements", "description": "heap on frequency counts."},
            {"title": "Merge k Sorted Lists", "description": "min-heap holding the current head of each list."},
            {"title": "Find Median from Data Stream", "description": "two heaps (max-heap for the lower half, min-heap for the upper half)."},
        ],
    },
    {
        "name": "Topological Sort",
        "how_it_works": (
            "Order the nodes of a directed acyclic graph (DAG) so that every edge points from "
            "an earlier node to a later one. Implemented via DFS (post-order, reversed) or BFS "
            "(Kahn's algorithm, using in-degree counts)."
        ),
        "recognition_signals": [
            "Keywords: \"prerequisites,\" \"course schedule,\" \"build order,\" \"dependency,\" \"task ordering.\"",
        ],
        "code_solution": '''from collections import deque

def can_finish(num_courses, prerequisites):
    # Build the graph: prereq -> course (an edge means "prereq must come first").
    # in_degree[course] = how many prerequisites still need to be completed.
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Kahn's algorithm: any course with in_degree 0 has no unmet
    # prerequisites, so it's safe to "take" right away.
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1  # we've successfully "completed" this course

        for neighbor in graph[node]:
            # Completing 'node' satisfies one prerequisite for 'neighbor'.
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                # neighbor now has zero unmet prerequisites — it's unlocked.
                queue.append(neighbor)

    # If we visited every course, there was no cycle blocking progress.
    # If a cycle exists, some courses never reach in_degree 0 and get skipped.
    return visited == num_courses
''',
        "example_problems": [
            {"title": "Course Schedule", "description": "determine if all courses can be finished (i.e., no cycle)."},
            {"title": "Course Schedule II", "description": "return a valid order."},
            {"title": "Alien Dictionary", "description": "derive character order from sorted word list, then topological sort."},
        ],
    },
    {
        "name": "Prefix Sum",
        "how_it_works": (
            "Precompute cumulative sums so that any subarray sum can be answered in O(1), "
            "instead of recomputing sums repeatedly."
        ),
        "recognition_signals": [
            "Keywords: \"range sum query,\" \"subarray sum equals k,\" \"multiple queries on a fixed array.\"",
        ],
        "code_solution": '''def subarray_sum(nums, k):
    # Key insight: if prefix_sum(right) - prefix_sum(left) == k, then the
    # subarray between left and right sums to k. Rearranged:
    # prefix_sum(left) == prefix_sum(right) - k.
    # So for each new prefix sum, we check how many earlier prefix sums
    # equal (current - k) — each one marks a valid subarray ending here.
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # empty prefix (sum 0) has occurred once, before we start

    for n in nums:
        prefix_sum += n

        # How many earlier positions had a prefix sum that makes a
        # k-summing subarray with the current position?
        count += seen.get(prefix_sum - k, 0)

        # Record that this prefix sum value has now occurred one more time.
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count
''',
        "example_problems": [
            {"title": "Range Sum Query - Immutable", "description": "precompute prefix sums, answer queries in O(1)."},
            {"title": "Subarray Sum Equals K", "description": "prefix sum + hash map counting how many times each prefix sum has occurred."},
            {"title": "Product of Array Except Self", "description": "prefix and suffix products."},
        ],
    },
    {
        "name": "Monotonic Stack / Queue",
        "how_it_works": (
            "Maintain a stack (or deque) where elements are kept in increasing or decreasing "
            "order, popping elements that violate the order as you scan. Great for \"next "
            "greater/smaller element\" style problems in O(n) instead of O(n²)."
        ),
        "recognition_signals": [
            "Keywords: \"next greater element,\" \"daily temperatures,\" \"largest rectangle,\" \"sliding window maximum.\"",
        ],
        "code_solution": '''def daily_temperatures(temps):
    result = [0] * len(temps)
    # The stack holds indices of days whose "warmer day" we haven't found yet.
    # Temperatures at those indices are kept in decreasing order from
    # bottom to top — that's the "monotonic" invariant.
    stack = []

    for i, t in enumerate(temps):
        # As long as today (t) is warmer than the day at the top of the
        # stack, we've just found that day's answer — pop and record it.
        # This is what makes the algorithm O(n): each index is pushed
        # and popped at most once across the whole run.
        while stack and temps[stack[-1]] < t:
            prev = stack.pop()
            result[prev] = i - prev  # number of days until it got warmer

        # Today might be the answer for some future day, so keep it around.
        stack.append(i)

    return result  # indices left on the stack never found a warmer day -> stay 0
''',
        "example_problems": [
            {"title": "Daily Temperatures", "description": "monotonic decreasing stack of indices, popping when a warmer day is found."},
            {"title": "Largest Rectangle in Histogram", "description": "monotonic stack tracking bar indices to find boundaries."},
            {"title": "Sliding Window Maximum", "description": "monotonic deque holding indices of useful candidates."},
        ],
    },
    {
        "name": "Trie (Prefix Tree)",
        "how_it_works": (
            "A tree structure where each path from root to a node represents a prefix. Enables "
            "fast prefix lookups and autocomplete-style queries."
        ),
        "recognition_signals": [
            "Keywords: \"prefix,\" \"autocomplete,\" \"word dictionary,\" \"search word with wildcards.\"",
        ],
        "code_solution": '''class TrieNode:
    def __init__(self):
        self.children = {}   # maps character -> next TrieNode
        self.is_end = False  # True if a word ends exactly at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()  # root represents the empty prefix

    def insert(self, word):
        node = self.root
        for ch in word:
            # setdefault: reuse the branch if it exists (shared prefix),
            # or create a new node if this is a new path — this sharing
            # of prefixes is exactly what makes a trie space-efficient.
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True  # mark that a full word terminates here

    def search(self, word):
        node = self.root
        for ch in word:
            # If any character along the way has no matching branch,
            # this word was never inserted.
            if ch not in node.children:
                return False
            node = node.children[ch]
        # We matched every character, but it's only a real match if a
        # word actually ENDS here (otherwise 'word' is just a prefix
        # of something longer that was inserted).
        return node.is_end
''',
        "example_problems": [
            {"title": "Implement Trie (Prefix Tree)", "description": "the base data structure."},
            {"title": "Word Search II", "description": "build a trie of the word list, DFS the grid while pruning against the trie."},
            {"title": "Design Add and Search Words Data Structure", "description": "trie with wildcard . matching via DFS."},
        ],
    },
    {
        "name": "Bit Manipulation",
        "how_it_works": (
            "Use bitwise operators (&, |, ^, ~, <<, >>) to solve problems in O(1) space/time "
            "that would otherwise need extra data structures."
        ),
        "recognition_signals": [
            "Keywords: \"single number,\" \"without extra space,\" \"power of two,\" \"count bits,\" constraints hint at using XOR tricks.",
        ],
        "code_solution": '''def single_number(nums):
    # XOR facts this relies on: a ^ a == 0, and a ^ 0 == a, and XOR is
    # commutative/associative (order doesn't matter). So every number
    # that appears twice cancels itself out (x ^ x = 0), and whatever
    # is left over is the number that appeared only once.
    result = 0
    for n in nums:
        result ^= n
    return result
''',
        "example_problems": [
            {"title": "Single Number", "description": "XOR all elements; duplicates cancel out."},
            {"title": "Number of 1 Bits", "description": "n & (n - 1) clears the lowest set bit."},
            {"title": "Counting Bits", "description": "DP using dp[i] = dp[i >> 1] + (i & 1)."},
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the LeetCode Pattern Guide tool with pattern data"

    def handle(self, *args, **options):
        tool, _ = Tool.objects.update_or_create(
            slug="leetcode-guide",
            defaults={
                "title": "LeetCode Study Techniques",
                "category": Tool.Category.GUIDE,
                "description": (
                    "Most coding interview problems aren't actually unique — they're variations "
                    "on a small set of recurring patterns. This guide covers the main patterns, "
                    "how to recognize them, and example problems for each."
                ),
                "url": "",
                "order": 1,
            },
        )
        tool.guide_patterns.all().delete()

        for i, p in enumerate(PATTERNS):
            pattern = GuidePattern.objects.create(
                tool=tool,
                name=p["name"],
                how_it_works=p["how_it_works"],
                recognition_signals=p["recognition_signals"],
                code_solution=p["code_solution"],
                code_language="python",
                order=i,
            )
            for j, ex in enumerate(p["example_problems"]):
                GuideExampleProblem.objects.create(
                    pattern=pattern,
                    title=ex["title"],
                    description=ex["description"],
                    url=ex.get("url", ""),
                    order=j,
                )

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(PATTERNS)} guide patterns."))
