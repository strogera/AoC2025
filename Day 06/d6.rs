use std::fs;

fn transpose(d: &[&str]) -> Vec<Vec<u64>> {
    let mut r = Vec::new();
    let mut c = Vec::new();
    let (rows, cols) = (d.len(), d[0].len());

    for i in 0..cols {
        let mut v = 0;
        let mut sp = true;

        for j in 0..rows {
            let b = d[j].as_bytes()[i];
            if b != b' ' {
                sp = false;
                v = v * 10 + (b - b'0') as u64;
            }
        }

        if sp {
            r.push(c);
            c = Vec::new();
        } else {
            c.push(v);
        }
    }
    r.push(c);
    r
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let (inp, ops) = input.trim().rsplit_once('\n').unwrap();
    let ops: Vec<&str> = ops.split_whitespace().collect();
    let inp = inp.lines().collect::<Vec<_>>();
    let p1: u64 = inp
        .iter()
        .map(|line| 
            line
                .split_whitespace()
                .map(|n| n.parse::<u64>().unwrap())
                .collect::<Vec<_>>())
        .reduce(|mut acc, line| {
            for i in 0..ops.len() {
                acc[i] = match ops[i] {
                    "+" => acc[i] + line[i],
                    _ => acc[i] * line[i],
                };
            }
            acc
        })
        .unwrap()
        .into_iter()
        .sum();
    let p2: u64 = transpose(&inp)
        .into_iter()
        .zip(&ops)
        .map(|(group, &op)|
            match op {
                "+" => group.iter().sum::<u64>(),
                _ => group.iter().product(),
            }
        )
        .sum();

    println!("{:?}", p1);
    println!("{:?}", p2);
}