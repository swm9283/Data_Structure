package pokemon;

public class Pokemon
{
    protected static int pokemonCount  = 0;
    protected String owner;
    protected String skills[];

    // 기본 생성자
    public Pokemon()
    {

    }

    // 매개변수 생성자.
    public Pokemon(String owner, String skills)
    {
        this.owner = owner;
        this.skills = skills.split("/");
        System.out.printf("포켓몬 생성:");
        pokemonCount = pokemonCount  + 1 ;

    }

    public String owner() //  Pokemon의 주인을 알려줍니다.
    {

        return owner;
    }

    public void info()
    {
        System.out.printf("%s의 포켓몬이 사용 가능한 스킬\n",this.owner);
        for(int i = 0 ; i<this.skills.length ; ++i)
        {
            System.out.printf(" %d : %s\n",i+1,skills[i]);
        }
    }

    public void attack(int idx)
    {
        System.out.printf(" %s 공격 시전!",skills[idx]);
    }




}
