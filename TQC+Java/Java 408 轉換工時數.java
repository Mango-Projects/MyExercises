/*
 * 1. 題目說明：
 * 請開啟C:\ANS.CSF\JP04資料夾中的JPD04.java進行編寫。依下列題意進行作答：輸入工時數，再輸出相對應的日期格式，使輸出值符合題意要求。檔案名稱請另存新檔為JPA04.java，儲存於C:\ANS.CSF\JP04資料夾，再進行評分。
 * 
 * 2. 設計說明：
 * (1) 請撰寫程式，讓使用者輸入工作總時數，輸入格式為時:分，時與分之間以一半形冒號隔開。一天工時為8小時，請依總工時計算，並輸出工作天數、小時、分鐘，如【2d:4h:0m】，中間以一個半形冒號分隔。若輸入文字或非法時間，請輸出【error】。
 * 
 * 3. 輸入輸出：
 * 輸入說明
 * 工作總時數，格式為時:分（時與分之間以一半形冒號隔開）
 * 
 * 輸出說明
 * 工時計算結果（輸出最後一行後不自動換行）
 * 
 * 
 * 範例輸入1
 * 20:00
 * 範例輸出1
 * 2d:4h:0m
 * 
 * 範例輸入2
 * 06:50
 * 範例輸出2
 * 0d:6h:50m
 * 
 * 範例輸入3
 * 5:01
 * 範例輸出3
 * 0d:5h:1m
 * 
 * 範例輸入4
 * 19:99
 * 範例輸出4
 * error
 */

import java.util.Scanner;

public class JPD04 {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        try {
            String[] input = scanner.next().split(":");
            int hours = Integer.parseInt(input[0]);
            int minutes = Integer.parseInt(input[1]);

            if (minutes > 59) {
                System.out.print("error");
                return;
            }
            System.out.printf("%dd:%dh:%dm", (int) (hours / 8), hours % 8, minutes);

        } catch (Exception ex) {
            System.out.print("error");
            return;
        }
    }
}
