class Solution:
    def entityParser(self, text: str) -> str:
        entity_to_c = {
            "&quot;" : "\"",
            "&apos;" : "'",
            "&amp;" : "&",
            "&gt;" : ">",
            "&lt;" : "<",
            "&frasl;" : "/"
        }

        text_list = []
        l = 0
        while l < len(text):
            if text[l] != "&":
                text_list.append(text[l])
                l += 1
                continue

            has_end = False
            for r in range(l + 1, l + 8):
                if r >= len(text):
                    break

                if text[r] != ";":
                    continue

                temp = self.changeEntity(entity_to_c, text[l: r + 1])
                if temp == "":
                    break
                
                has_end = True
                text_list.append(temp)
                l = r + 1
                break
                
            if has_end == False:
                text_list.append(text[l])
                l += 1

        return "".join(text_list)

    def changeEntity(self, entity_to_c: dict[str, str], text: str) -> str:
        if text in entity_to_c:
            return entity_to_c[text]
        return ""
    
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: 官方範例
    s1 = "&amp; is an HTML entity but &ambassador; is not."
    expected1 = "& is an HTML entity but &ambassador; is not."
    assert sol.entityParser(s1) == expected1, f"Test1 Fail: got {sol.entityParser(s1)}"

    # Test case 2: 多個不同實體
    s2 = "Stay &lt;coding&gt; &amp; have fun!"
    expected2 = "Stay <coding> & have fun!"
    assert sol.entityParser(s2) == expected2, f"Test2 Fail: got {sol.entityParser(s2)}"

    # Test case 3: 實體沒有結束符號
    s3 = "5 &lt 6 &amp 7"
    expected3 = "5 &lt 6 &amp 7"
    assert sol.entityParser(s3) == expected3, f"Test3 Fail: got {sol.entityParser(s3)}"

    # Test case 4: 連續實體
    s4 = "&quot;&apos;&frasl;&quot;"
    expected4 = "\"'/\""
    assert sol.entityParser(s4) == expected4, f"Test4 Fail: got {sol.entityParser(s4)}"

    # Test case 5: 沒有任何實體
    s5 = "hello world"
    expected5 = "hello world"
    assert sol.entityParser(s5) == expected5, f"Test5 Fail: got {sol.entityParser(s5)}"

    # Test case 6: 偽實體，不在列表裡
    s6 = "hello &abcefg; world"
    expected6 = "hello &abcefg; world"
    assert sol.entityParser(s6) == expected6, f"Test6 Fail: got {sol.entityParser(s6)}"

    # Test case 7: 開頭結尾都是實體
    s7 = "&lt;hello world&gt;"
    expected7 = "<hello world>"
    assert sol.entityParser(s7) == expected7, f"Test7 Fail: got {sol.entityParser(s7)}"

    print("All tests passed!")