# Enter your code here. Read input from STDIN. Print output to STDOUT


def get_neighbors(r, c, rows, cols):
    # 8-direction neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def count_8_connected_objects(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]

    def dfs(r, c):
        stack = [(r,c)]
        visited[r][c] = True
        while stack:
            rr, cc = stack.pop()
            for nr, nc in get_neighbors(rr, cc, rows, cols):
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    stack.append((nr,nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                count += 1
    return count


if __name__ == "__main__":
    # Input grid as given
    grid = [
        [0,0,0,1,1,0,0,0,1,0,1,0],
        [1,1,1,0,1,1,1,1,0,0,0,1],
        [1,1,1,0,1,0,0,1,0,0,1,0],
        [1,0,0,0,0,0,0,0,1,0,0,0]
    ]

    print(count_8_connected_objects(grid))