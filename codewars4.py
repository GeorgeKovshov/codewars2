def bouncing_ball(h, bounce, window):
    if h <= 0 or window >= h or bounce >= 1 or bounce <= 0:
        return -1
    else:
        result = 1
        h = h * bounce
        while h > window:
            result += 2
            h = h * bounce
        return result


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
