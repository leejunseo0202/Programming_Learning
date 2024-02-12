import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int meozation[][] = new int[41][2];

    public static void settingFibonacci() {
        meozation[0][0] = 1; meozation[0][1] = 0;
        meozation[1][0] = 0; meozation[1][1] = 1;

        for (int i = 2; i < 41; i++) {
            meozation[i][0] = meozation[i - 1][0] + meozation[i - 2][0];
            meozation[i][1] = meozation[i - 1][1] + meozation[i - 2][1];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int i = Integer.parseInt(br.readLine());
        for (; i > 0; i--) {
            int num = Integer.parseInt(br.readLine());
            settingFibonacci();

            String count_0 = String.valueOf(meozation[num][0]);
            String count_1 = String.valueOf(meozation[num][1]);

            bw.write(count_0 + " " + count_1 + "\n");
        }

        bw.close();
    }
}