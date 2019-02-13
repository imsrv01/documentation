public class FIZZBUZZ{

     public static void main(String []args){
        int n=50;
        System.out.println("Multiple of 3 or 5");
        for (int i=1; i <= n ; i++) {
            //System.out.println(i);
            if ( i%3 ==0 & i%5 == 0) {
                System.out.print("FIZZBUZZ" + ",");
            } else if (i % 3 == 0) {
                System.out.print("FIZZ" + ",");
            } else if (i % 5 == 0) {
                System.out.print("BUZZ" + ",");
            } else {
                System.out.print(i + ",");
            }
        }
        
        System.out.println("----");
        System.out.println("Replace number ending with digit 3 (FIZZ) or 5 (BUZZ)");
        
        for (int i=1; i <= n ; i++) {
            //System.out.println(i);
            if ( i%10 ==3 ) {
                System.out.print("FIZZ" + ",");
            } else if (i % 10 == 5) {
                System.out.print("BUZZ" + ",");
            } else {
                System.out.print(i + ",");
            }
        }
        
        System.out.println("----");
        System.out.println("Replace number containing digit 3 (FIZZ) or 5 (BUZZ)");
        for (int i=1; i <= n; i++) {
            int num=i;
            while (num > 0) {
                if (num%10 == 3) {
                    System.out.print("FIZZ" + ",");
                    break;
                } else if (num%10 == 5) {
                    System.out.print("BUZZ" + ",");
                    break;
                } else {
                    num = num/10;
                    if (num <= 0) {
                        System.out.print(i + ",");
                    }
                }
            }    
        }
     }
}
