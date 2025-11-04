"""
- import sys: 표준 입력(stdin)과 같은 저수준 파일 객체에 접근하기 위해 사용합니다.
- input = sys.stdin.readline: 내장 input() 함수 호출을 표준 입력의 readline 메서드로 재지정하여

- 코딩테스트에서는 입력 데이터가 매우 큰 경우가 많아
    Python의 기본 내장 input() 함수가 느려서 시간 초과(TLE)가 발생할 수 있습니다.
    내장 input()은 추가적인 처리(overhead)가 포함되어 있어 많은 호출이 모이면 비용이 커집니다.
- sys.stdin.readline은 C 레벨의 버퍼에서 한 줄을 빠르게 읽어오는 저수준 함수로,
    불필요한 추가 처리(overhead)가 적어 대량 입력 처리에 적합합니다.
어떻게 작동하는가?
- sys.stdin은 운영체제와 연결된 표준 입력을 감싼 파일 객체(file-like object)입니다.
- sys.stdin.readline(): 표준 입력에서 다음 줄을 한 번에 읽어와 문자열로 반환합니다.
    반환 문자열은 끝에 개행 문자('\n')를 포함하고 있으므로 필요에 따라 제거해야 합니다.
- input = sys.stdin.readline: 이후 코드에서 input()을 호출하면 내장 input 대신
    sys.stdin.readline이 호출됩니다. 즉, 기존 코드 구조나 함수 호출을 바꾸지 않고
    입력 속도만 개선할 수 있습니다.
"""
import sys
input = sys.stdin.readline

# 버블 정렬
# 시간 복잡도: O(n^2)
'''n = int(input())
arr = [int(input()) for _ in range(n)]
for i in range(n - 1):
    for j in range(0, n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]'''
# 선택 정렬 (Selection Sort)
# 시간 복잡도: O(n^2)
'''def selection_sort(a):
    a = a[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
arr = selection_sort(arr)'''
# 삽입 정렬 (Insertion Sort)
# 시간 복잡도: O(n^2)
'''def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a
arr = insertion_sort(arr)'''
# 병합 정렬 (Merge Sort)
# 시간 복잡도: O(n log n)
'''def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    if i < len(left): res.extend(left[i:])
    if j < len(right): res.extend(right[j:])
    return res'''
# 퀵 정렬 (Quick Sort)
# 시간 복잡도: 평균 O(n log n), 최악 O(n^2)
'''def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr = quick_sort(arr)'''
# 힙 정렬 (Heap Sort)
# 시간 복잡도: O(n log n)
'''import heapq
def heap_sort(a):
    h = a[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
arr = heap_sort(arr)'''

n = int(input())
arr = [int(input()) for _ in range(n)]
# 파이썬 내장 정렬 (Timsort) 
# 시간 복잡도: O(n log n)
arr.sort()
sys.stdout.write('\n'.join(map(str, arr)) + '\n')
