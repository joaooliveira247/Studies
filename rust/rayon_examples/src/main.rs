use rayon::ThreadPoolBuilder;
use rayon::prelude::*;

const THREAD_NUMS: usize = 4;

fn main() {
    ThreadPoolBuilder::new()
        .num_threads(THREAD_NUMS)
        .build_global()
        .unwrap();

    let nums = vec![1, 2, 3, 4, 5];

    let squares: Vec<i32> = nums.par_iter().map(|&num| num * num).collect();

    println!("Square of {:?}: {:?}", nums, squares)
}
