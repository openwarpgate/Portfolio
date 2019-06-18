#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int turnCount;

struct Player
{
	char name[20];
	int hp;
	int maxhp;
	int sp;
	int maxsp;
	int mp;
	int maxmp;
	int positionX;
	int positionY;

	//items
	int items[100];

	//for process command
	int userStatus; 
	int command;
}me;

void Render()
{
	if (me.userStatus == 0)
	{
		printf("지금은 %d 턴입니다.\n", turnCount);
		printf("지금 위치는 (%d, %d) 입니다\n", me.positionX, me.positionY);
		printf("지금 체력는 (%d / %d) 입니다\n", me.hp, me.maxhp);
		printf("지금 마력는 (%d / %d) 입니다\n", me.mp, me.maxmp);
		printf("지금 지구력는 (%d / %d) 입니다\n", me.sp, me.maxsp);
		printf("행동을 선택해 주십시오\n");
		printf("1. 이동, 2. 아이템 정비\n");
	}
	else if (me.userStatus == 1)
	{
		
	}
	else if (me.userStatus == 2)
	{
		
	}
}

void ProcessInput()
{
	while (1)
	{
		if (me.userStatus == 0)
		{
			scanf("%d", &me.command);
			if (me.command == 1)
			{
				me.userStatus = 1;
			}
			else if (me.command == 2)
			{
				me.userStatus = 2;
			}
		}
		else if (me.userStatus == 1)
		{
			printf("이동 방향을 선택하세요\n");
			printf("1. 동, 2. 서, 3. 남, 4. 북");
			scanf("%d", &me.command);
			if (me.command == 1)
			{
				me.positionX += 1;
				me.sp -= 1;
			}
			else if (me.command == 2)
			{
				me.positionX -= 1;
				me.sp -= 1;
			}
			else if (me.command == 3)
			{
				me.positionY += 1;
				me.sp -= 1;
			}
			else if (me.command == 4)
			{
				me.positionX -= 1;
				me.sp -= 1;
			}
			me.userStatus = 0;
			break;
		}
		else if (me.userStatus == 2)
		{
			printf("아이템 목록\n");
			for (int i = 0; i < 10; i++)
			{
				for (int j = 0; j < 10; j++)
				{
					printf("%5d", me.items[i * 10 + j]);
				}
				printf("\n");
			}
			printf("계속 하려면 아무 키나 입력하세요\n");
			scanf("%d", &me.command);
			me.userStatus = 0;
			turnCount--;
			break;
		}
	}
	
}

void ModifyGameState()
{
	turnCount+=1;
}

void Initialize()
{
	printf("이름을 입력하세요\n");
	scanf("%s", me.name);
	printf("당신의 이름은 %s 입니다\n", me.name);
	me.hp = 100;
	me.maxhp = 100;
	me.mp = 100;
	me.maxmp = 100;
	me.sp = 100;
	me.maxsp = 100;
	me.positionX = 0;
	me.positionY = 0;
	me.userStatus = 0;
}

void GameLoop()
{
	while (1)
	{
		Render();
		ProcessInput();
		ModifyGameState();
	}
}
int main()
{
	Initialize();
	GameLoop();
	return 0;
}
