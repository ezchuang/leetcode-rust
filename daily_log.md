# START
11/10 參考[別人的 Structure](https://github.com/aylei/leetcode-rust) 建立 Leetcode 作答紀錄的 repo，想要依照 Rustdoc 與 compiler 的 err msg 提示與 Google(and AI) 嘗試自己逐步解答題目，藉此熟悉 Rust 的語法與用法。

# Log
- 11/10 
  - 完成 0001 與 0002
  - 練習操作 HashMap，其中對於 Option 的操作跟 Java 的 Optional 差很多。
  - 不是很會操作指標(忘光了)，接近盲試的讓等號兩邊的變數型別匹配
    - Java:
        - x.get(): 可能取到 null，用 'if (x.isPresent())' prevent
        - x.isPresent(value -> ...): lambda expression, not closure (Java 的 lambda 僅能使用外部 final 變數)
        - orElse(default)
        - orElseGet(lambda expression, get value when that variable is null)
        - orElseThrow(() -> new IllegalStateException("No value present"))
    - Rust 中為 Enum，包含 Some / None
        - match: switch case in Java, R
        - x.unwrap(): 直接取值。若為 None 會 panic
        - x.unwrap_or(default)
        - x.unwrap_or_else(closure)
        - x.expect(msg): 為 None 時，return 傳入的 err msg

- 11/11
    - 完成 0009
    - 數字與字串 (String & Char) 相對容易理解，多嘗試了幾種方法 (iterator / string as bytes / 數值計算)
    - 未來的我記得回來複習 iterator & string as bytes

- 11/12
    - 完成 0013
    - 嘗試不可變借用 (&) 功能
    - 嘗試用 vec 生成 HashMap (暫時沒看到更漂亮的方法)

- 11/13
    - 完成 0020

- 11/14
    - 沒完成 0021
    - 今天時間比較短，且想盡可能不調查網路情報、依據手邊資料完成題目，所以沒有完成他，隔天繼續
    - 待補研究心得

- 11/15
    - 完成 0021
    - 待補

- 11/16
    - 檢討與新增 0021 的 Solution
    - 待補

- 11/17
    - 檢討與新增 0021 的 Solution & 完成 0024
    - 待補

- 11/18
    - 寫錯 0031，明天繼續；針對題型沒有想清楚