impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut bestcontainer = 0;
        let mut p1 = 0;
        let mut p2 = height.len() - 1;

        while p1 < p2 {
            let w = p2 - p1;
            let h = height[p1].min(height[p2]);
            let area = w * h as usize;

            bestcontainer = bestcontainer.max(area as i32);

            if height[p1] < height[p2] {
                p1 += 1;
            } else {
                p2 -= 1;
            }
        }

        bestcontainer
    }
}
