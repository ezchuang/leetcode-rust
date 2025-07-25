from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {
            0: 0,
            1: 0
        }
        for favor in students:
            count[favor] += 1

        while sandwiches:
            if any(amount == 0 for amount in count.values()) and students[0] != sandwiches[0]:
                break
            if students[0] == sandwiches[0]:
                count[students[0]] -= 1
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))

        return len(students)
    
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: 全部都能吃到
    students1 = [1, 1, 0, 0]
    sandwiches1 = [0, 1, 0, 1]
    expected1 = 0
    assert sol.countStudents(students1[:], sandwiches1[:]) == expected1, f"Test1 Fail: got {sol.countStudents(students1[:], sandwiches1[:])}"

    # Test case 2: 有人永遠吃不到
    students2 = [1, 1, 1, 0, 0, 1]
    sandwiches2 = [1, 0, 0, 0, 1, 1]
    expected2 = 3
    assert sol.countStudents(students2[:], sandwiches2[:]) == expected2, f"Test2 Fail: got {sol.countStudents(students2[:], sandwiches2[:])}"

    # Test case 3: 沒有學生
    students3 = []
    sandwiches3 = []
    expected3 = 0
    assert sol.countStudents(students3, sandwiches3) == expected3, f"Test3 Fail: got {sol.countStudents(students3, sandwiches3)}"

    # Test case 4: 沒有人喜歡第一個三明治
    students4 = [1, 1, 1]
    sandwiches4 = [0, 1, 1]
    expected4 = 3
    assert sol.countStudents(students4[:], sandwiches4[:]) == expected4, f"Test4 Fail: got {sol.countStudents(students4[:], sandwiches4[:])}"

    # Test case 5: 所有人都喜歡相同口味
    students5 = [0, 0, 0]
    sandwiches5 = [0, 0, 0]
    expected5 = 0
    assert sol.countStudents(students5[:], sandwiches5[:]) == expected5, f"Test5 Fail: got {sol.countStudents(students5[:], sandwiches5[:])}"

    print("All tests passed!")