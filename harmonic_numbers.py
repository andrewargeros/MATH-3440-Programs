def harmonic(n):
  """
  Returns the nth harmonic number using recursion.
  """
  if n < 1:
    return 0
  else:
    return 1 / n + harmonic(n - 1)

print(harmonic(1)), print(harmonic(2)), print(harmonic(3))