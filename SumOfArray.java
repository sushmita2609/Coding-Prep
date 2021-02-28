package code_probs;
import java.util.Arrays;
import java.util.Scanner;
public class SumOfArray {
   public static void main(String args[]){
      
      Scanner s = new Scanner(System.in);
      int size = s.nextInt();
      int myArray[] = new int [size];
      int sum = 0;
      for(int i=0; i<size; i++){
         myArray[i] = s.nextInt();
         sum = sum + myArray[i];
      }
      System.out.println(sum);
   }
}