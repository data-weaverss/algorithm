def solution(sizes):
    max_width, max_height = 0, 0
    for i in range(len(sizes)):
        w, h = sizes[i]
        if w < h:
            w, h = h, w
        max_width = max(w, max_width)
        max_height = max(h, max_height)
    return max_width * max_height