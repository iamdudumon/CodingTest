//https://www.acmicpc.net/problem/2812
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

class Pair{
    int num;
    boolean state;

    Pair(int num, boolean state) {
        this.num = num;
        this.state = state;
    }
}

public class Main {
    public static void main(String[] args) throws IOException{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            String num = br.readLine();

            List<Pair> nums = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                nums.add(new Pair((int) num.charAt(i) - '0', true));
            }
            int i = 0, count = 0, j = 1, stack = 0;

            while (count < k) {
                if (j == n) {
                    int t = i;
                    while (count < k) {
                        if (nums.get(t).state) {
                            nums.get(t).state = false;
                            count++;
                        }
                        t--;
                    }
                    break;
                }

                if ((int) (num.charAt(i) - '0') < (int) (num.charAt(j) - '0') && nums.get(i).state) {
                    nums.get(i).state = false;
                    count++;

                    if (count != j) {
                        i--;
                    } else {
                        i = j;
                        j = i + 1;
                    }
                }else if((int) (num.charAt(i) - '0') < (int) (num.charAt(j) - '0') && !nums.get(i).state){
                    i--;
                }
                else {
                    i = j;
                    j = i + 1;
                }

            }

            StringBuilder answer = new StringBuilder();
            for (Pair pair : nums) {
                if (pair.state)
                    answer.append(pair.num);
            }
            System.out.println(answer.toString());

    }

}
