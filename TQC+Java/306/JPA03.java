import java.util.Scanner;

public class JPA03 {
	public static void main(String args[]) {
		int a[][] = { { 1, 2, 3 }, { 4, 5, 6 } };
		int b[][] = new int[2][3];
		int c[][] = new int[2][3];
		Scanner scanner = new Scanner(System.in);
		String str = scanner.nextLine();
		String[] a1 = str.split(" ");
		
		if (a1.length < 6) {
			System.out.print("error");
			return;
		}

		int k = 0;
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 3; j++)
				try {
					b[i][j] = Integer.parseInt(a1[k]);
					k++;
				} catch (Exception e) {
					System.out.print("error");
					return;
				}
		}
		compute(a, b, c);
		print(c);
	}

	public static void compute(int[][] a, int[][] b, int c[][]) {
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 3; j++)
				c[i][j] = a[i][j] + b[i][j];
	}

	public static void print(int[][] s) {
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 3; j++)
				System.out.printf("%4d", s[i][j]);
			System.out.println("");
		}
	}
}