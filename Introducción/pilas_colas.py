# pila/stack -> el ultimo elemento es primero en eliminarlo

stack = []
stack.append("google.com")
stack.append("amazon.com")
stack.append("facebook.com")
print(f"urls: {stack}")

# método pop manual
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)
print(f"urls: {stack}")

# elimine el segundo item
stack_item2 = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item2)
print(f"urls: {stack}")

# método pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# cola/queue -> se elimina el elemento primer elemento de un lista

print("-------------queue--------------")
queue = []
queue.append("google.com")
queue.append("amazon.com")
queue.append("facebook.com")
print(f"urls: {queue}")

# método manual de pop
queue_item = queue[0]
print(queue_item)
del queue[0]

# método pop
print(queue.pop(0))
print(f"urls: {queue}")
