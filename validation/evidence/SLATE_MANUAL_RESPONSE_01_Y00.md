An **array** stores multiple values of the same type in one object.

Inside a method:
```
int[] A = {10, 20, 30};
```

Exact terms:

- `A` is a variable of type `int[]`.
- The array itself is an **object of indexed components**.
- `A` holds a **reference** to that array object; it does not directly contain the three integers.
- An **index** selects one component.
- Java array indexes start at `0`.

So:
```yaml
index:   0   1   2
         ↓   ↓   ↓
A  →   [10, 20, 30]
```

Therefore, inside the same method:
```
int x = A[0];
```

`A[0]` means **the component of array `A` at index `0`**, so `x` becomes `10`.

Now a fresh array:
```
int[] B = {7, 14, 21, 28};
```

**What value does `B[2]` give?**
