def union(A, B):
    # A와 B를 집합으로 변환하여 합집합을 구한 후 리스트로 변환
    return list(set(A) | set(B))

def intersection(A, B):
    # A와 B를 집합으로 변환하여 교집합을 구한 후 리스트로 변환
    return list(set(A) & set(B))

def difference(A, B):
    # A와 B를 집합으로 변환하여 차집합을 구한 후 리스트로 변환
    return list(set(A) - set(B))

A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

# 집합 연산 수행
union_result = union(A, B)
intersection_result = intersection(A, B)
difference_result = difference(A, B)

# 결과 출력
print("합집합:", union_result)
print("교집합:", intersection_result)
print("차집합 (A - B):", difference_result)
