fn twentyfour() -> String {
    let digits: [usize; 10] = core::array::from_fn(|i| i);
    let s_digits = digits
        .iter()
        .map(|x| x.to_string())
        .collect();

    fn f(u_list: Vec<String>) -> Vec<String>{
        let mut new: Vec<String> = Vec::new();
        for val in u_list {
            for i in 0..10 {
                let i_string = i.to_string();
                let mut k = val.to_string();
                if !(k.contains(&i_string)) {
                    k.push_str(&i_string);
                    new.push(k);
                };
            }
        }
        new
    }

    f(f(f(f(f(f(f(f(f(s_digits)))))))))[999999].clone()
}

fn thirty() -> usize {
    for i in range(2, 10**21):
        if i == sum(k**5 for k in list(map(int, list(str(i))))):
            print(i)
}

fn main() {
    println!("{:?}", twentyfour());
}
