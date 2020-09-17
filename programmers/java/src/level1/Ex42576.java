package level1;

import java.util.HashMap;
import java.util.Map;

/**
 * 문제 설명 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
 *
 * <p>마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을
 * return 하도록 solution 함수를 작성해주세요.
 *
 * <p>제한사항 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다. completion의 길이는 participant의 길이보다 1 작습니다. 참가자의
 * 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다. 참가자 중에는 동명이인이 있을 수 있습니다.
 */
public class Ex42576 {
  public String solution(String[] participant, String[] completion) {
    String answer = "";

    final HashMap<String, Integer> count = new HashMap<>();

    for (String name : participant) {
      count.put(name, count.getOrDefault(name, 0) + 1);
    }

    for (String name : completion) {
      count.put(name, count.get(name) - 1);
    }

    for (Map.Entry<String, Integer> entry : count.entrySet()) {
      if (entry.getValue() != 0) {
        answer = entry.getKey();
        break;
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    final Ex42576 ex = new Ex42576();

    final String[] participant = {"leo", "kiki", "eden"};
    final String[] completion = {"eden", "kiki"};
    System.out.println(ex.solution(participant, completion)); // leo

    final String[] participant2 = {"marina", "josipa", "nikola", "vinko", "filipa"};
    final String[] completion2 = {"josipa", "filipa", "marina", "nikola"};
    System.out.println(ex.solution(participant2, completion2)); // vinko
  }
}
