import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class JPA05 {
	static Scanner sanner = new Scanner(System.in);

	public static void main(String[] args) {

		String[] new_student = { "Sam", "1981/10/1", "A234567890" };

		try {
			String[] input = sanner.nextLine().split(" ");
			for (String string : input) {
				int number = Integer.parseInt(string);
				if (number > 100 || number < 0) {
					System.out.print("error");
					return;
				}
			}
			String text = String.format("%s,%s,%s,%s,%s,%s", new_student[0], new_student[1], new_student[2], input[0], input[1], input[2]);
			System.out.print(text);

			File file = new File("write.txt");
			FileWriter fileWriter = new FileWriter(file);
			fileWriter.write(text + "\r\n");
			fileWriter.close();
		} catch (Exception ex) {
			System.out.print("error");
			return;
		}
	}
}