public class Problem1{
    int sum;
    private int sumTo; 

    public Problem1(int num){
        sumTo = num;
        sum = 0;
    }

    public int sum_factors(){
        for(int i = 0; i < sumTo; i++){
            if(i % 3 == 0 || i % 5 == 0){
                sum += i; 
            }
        }
        return sum;
    }

    public static void main(String[] args){
        Problem1 prob = new Problem1(1000);
        System.out.println(prob.sum_factors());
    }

}