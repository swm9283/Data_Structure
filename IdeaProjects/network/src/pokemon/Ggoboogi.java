package pokemon;

public class Ggoboogi extends Pokemon
{
    protected String name;
    //기본 생성자.
    public Ggoboogi() {}
    // 매개변수 생성자.
    public Ggoboogi(String owner, String skills)
    {
        super.owner = owner;
        super.skills = skills.split("/");
        this.name = "꼬부기";
        System.out.printf("포켓몬 생성: %s\n",this.name);
        super.pokemonCount = super.pokemonCount + 1 ;
    }
    public void attack(int idx)
    {
        System.out.printf("[꼬북꼬북] %s의 %s가 %s 공격시전!\n",this.owner,this.name,this.skills[idx]);
    }
}

