package pokemon;

public class Pikachu extends Pokemon
{
    protected String name;
    // 매개변수 생성자.
    public Pikachu(String owner, String skills)
    {
        super.owner = owner;
        super.skills = skills.split("/");
        this.name = "피카츄";
        System.out.printf("포켓몬 생성: %s\n",this.name);
        super.pokemonCount = super.pokemonCount + 1 ;
    }
    public void attack(int idx)
    {
        System.out.printf("[피카피카] %s의 %s가 %s 공격시전!\n",this.owner,this.name,this.skills[idx]);
    }
}
