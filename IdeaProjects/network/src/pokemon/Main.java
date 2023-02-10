package pokemon;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.printf("총 %d마리의 포켓몬이 생성되었습니다.\n", Pokemon.pokemonCount);
            System.out.print("1) 포켓몬 생성 2) 프로그램 종료 : ");
            int menu = sc.nextInt();
            sc.nextLine();
            if (menu == 2) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else if (menu == 1) {
                System.out.print("1) 피카츄 2) 꼬부기 3) 파이리");
                int pokemon = sc.nextInt();
                sc.nextLine();
                System.out.print("플레이어 이름을 입력하세요! : ");
                String name = sc.nextLine();
                System.out.print("사용 가능한 기술입력(/로 구분하여 입력) : ");
                String skill = sc.nextLine();
                if (pokemon == 1) {
                    Pikachu p = new Pikachu(name, skill);
                    p.info();
                    System.out.print("공격 번호 선택 : ");
                    int idx = sc.nextInt();
                    p.attack(idx-1);
                } else if (pokemon == 2) {
                    Ggoboogi p = new Ggoboogi(name, skill);
                    p.info();
                    System.out.print("공격 번호 선택 : ");
                    int idx = sc.nextInt();
                    p.attack(idx-1);

                } else if (pokemon == 3) {
                    Pairi p = new Pairi(name, skill);
                    p.info();
                    System.out.print("공격 번호 선택 : ");
                    int idx = sc.nextInt();
                    p.attack(idx-1);

                } else {
                    System.out.println("메뉴에서 선택해주세요");
                }

            } else {
                System.out.println("메뉴에서 선택해주세요");
            }


        }

    }
}