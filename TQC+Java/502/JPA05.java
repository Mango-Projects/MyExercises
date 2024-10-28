import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class JPA05 {
	static Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) {

		try {
			String input = scanner.nextLine();
			if (input == "") {
				System.out.print("error");
				return;
			}

			File file = new File("write.txt");
			FileWriter fileWriter = new FileWriter(file);

			fileWriter.write(input);
			fileWriter.close();
			
			Scanner reader = new Scanner(file);
			System.out.print("write:" + reader.nextLine());
			reader.close();
		} catch (Exception error) {
			System.out.print("error");
			return;
		}
	}
}
