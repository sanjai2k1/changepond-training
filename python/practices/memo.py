from collections import deque

def is_balanced(s):
    # Check if all 'a's come before any 'b's
    seen_b = False
    for char in s:
        if char == 'b':
            seen_b = True
        elif seen_b and char == 'a':
            return False
    return True

def process_string(s):
    queue = deque([(s, 0)])
    visited = set([s])

    while queue:
        current_str, steps = queue.popleft()

        if is_balanced(current_str):
            print((current_str, steps))
            break

        # Process all possible removals
        for i in range(len(current_str)):
            if current_str[i] == 'a' and 'b' in current_str[i+1:]:
                b_index = current_str[i+1:].index('b') + i + 1
                new_str = current_str[:b_index] + current_str[b_index+1:]
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append((new_str, steps + 1))

            if current_str[i] == 'b' and 'a' in current_str[i+1:]:
                a_index = current_str[i+1:].index('a') + i + 1
                new_str = current_str[:a_index] + current_str[a_index+1:]
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append((new_str, steps + 1))

# Example usage
s = "bbaaaaabb"
process_string(s)
