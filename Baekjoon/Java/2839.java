import java.io.*;
import java.util.Scanner;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Bag{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int bag_5=0, bag_3=0, weight;

    public Bag()  throws IOException{weight = Integer.parseInt(br.readLine());}
    public void calculate() throws IOException{
        int bag_5 = weight / 5;
        for(;bag_5>=0;bag_5--){
            bag_3 = (weight - bag_5 * 5) / 3;

            if((bag_5 * 5 + bag_3 * 3) == weight){
                bw.write(String.valueOf(bag_5 + bag_3));

                br.close();bw.close();
                return;
            }
        }
        bw.write("-1");
        br.close();bw.close();
    }
}

public class Main{
    public static void main(String[] args)  throws IOException{
        Bag bag = new Bag();

        bag.calculate();
    }
}