package pokemon;

public class Pairi extends Pokemon
{
    protected String name;
    //기본 생성자.
    public Pairi() {}
    // 매개변수 생성자.
    public Pairi(String owner, String skills)
    {
        super.owner = owner;
        super.skills = skills.split("/");
        this.name = "파이리";
        System.out.printf("포켓몬 생성: %s\n",this.name);
        super.pokemonCount = super.pokemonCount + 1 ;
    }
    public void attack(int idx)
    {
        System.out.printf("[파일파일] %s의 %s가 %s 공격시전!\n",this.owner,this.name,this.skills[idx]);
    }
}

