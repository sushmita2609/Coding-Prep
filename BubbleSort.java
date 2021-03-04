package code_probs;
import java.io.*;
public class BubbleSort {
	static void sort_arr(int arr[], int n)
	{
		int i, j, temp;
		boolean swapped;
		for(i=0;i<n-1;i++)
		{
			swapped=false;
			for(j=0;j<n-i-1;j++)
			{
				if(arr[j]>arr[j+1])
				{
					temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
					swapped=true;
				}
			}
			if(swapped == false)
				break;
		}
	}
	static void printArray(int arr[], int size)
	{
		int i;
		for(i=0;i<size;i++)
			System.out.print(arr[i]+" ");
		System.out.println();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
       int arr[] = {64, 23, 10, 40, 5};
       int n= arr.length;
       System.out.println("Given");
       printArray(arr,n);
       
       sort_arr(arr, n);
       System.out.println("array");
       printArray(arr,n);
	}

}
