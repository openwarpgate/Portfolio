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
		printf("������ %d ���Դϴ�.\n", turnCount);
		printf("���� ��ġ�� (%d, %d) �Դϴ�\n", me.positionX, me.positionY);
		printf("���� ü�´� (%d / %d) �Դϴ�\n", me.hp, me.maxhp);
		printf("���� ���´� (%d / %d) �Դϴ�\n", me.mp, me.maxmp);
		printf("���� �����´� (%d / %d) �Դϴ�\n", me.sp, me.maxsp);
		printf("�ൿ�� ������ �ֽʽÿ�\n");
		printf("1. �̵�, 2. ������ ����\n");
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
			printf("�̵� ������ �����ϼ���\n");
			printf("1. ��, 2. ��, 3. ��, 4. ��");
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
			printf("������ ���\n");
			for (int i = 0; i < 10; i++)
			{
				for (int j = 0; j < 10; j++)
				{
					printf("%5d", me.items[i * 10 + j]);
				}
				printf("\n");
			}
			printf("��� �Ϸ��� �ƹ� Ű�� �Է��ϼ���\n");
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
	printf("�̸��� �Է��ϼ���\n");
	scanf("%s", me.name);
	printf("����� �̸��� %s �Դϴ�\n", me.name);
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
