while True:
  try:
    n, k = map(int, input().split())
    coupon = n
    while n >= k:
      coupon += n//k
      n = n // k + (n % k)
    print(coupon)
  except:
    break
