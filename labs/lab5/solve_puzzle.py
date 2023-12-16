def solve_puzzle(tiles, tiles_cache=None, current_index=0): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    # 1) Base case: have you found a valid solution?
    if tiles_cache is None: tiles_cache = {}
    n = tiles[current_index]
    if (current_index in tiles_cache.keys()) or (n == 0): return current_index

    # 2) Find all valid next-steps
    if current_index not in tiles_cache.keys():
        next_index_cw, next_index_ccw = ((current_index + n) % len(tiles)), ((current_index - n) % len(tiles))
        if next_index_ccw < 0: next_index_ccw = len(tiles) + next_index_ccw
        tiles_cache[current_index] = ()
        tiles_cache[current_index] = (solve_puzzle(tiles, tiles_cache, next_index_cw), solve_puzzle(tiles, tiles_cache, next_index_ccw))

    # 3) Recursively explore next-steps, returning True if any valid solution is found
    if any((len(tiles)-1) in i for i in tiles_cache.values()): return True
    else: return False