impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut first: usize = 0;
        let mut second: usize = numbers.len() - 1;

        while first < second {
            if numbers[first] + numbers[second] == target {
                break;
            } else if numbers[first] + numbers[second] < target {
                first += 1;
            } else {
                second -= 1;
            }
        }
        return Vec::from([first as i32 + 1, second as i32 + 1]);
    }
}
