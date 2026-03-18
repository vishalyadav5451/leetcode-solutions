class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [str(i) for i in (range(1,n+1))]
        
        for i in range (len(arr)):
            num = int(arr[i])
            if num % 3 == 0 and num % 5 == 0 :
                arr[i] = "FizzBuzz"
            elif   num % 3 == 0 :
                arr[i] = "Fizz"
            elif num % 5 == 0 :
                arr[i] = "Buzz" 
        return arr

