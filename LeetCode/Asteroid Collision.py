def asteroidCollision(asteroids):
    stack = []
    for ast in asteroids:
        while stack and ast < 0 and stack[-1] > 0:
            differ = ast + stack[-1]
            if differ < 0:
                stack.pop()
            elif differ > 0:
                ast = 0
            else:
                ast = 0
                stack.pop()
        if ast:
            stack.append(ast)
    return stack


print(asteroidCollision([5, 10, -5]))
print(asteroidCollision([8,-8]))
