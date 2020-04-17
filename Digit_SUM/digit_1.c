/*输入两个非负整数，按照逆序存入A、B两个链表中，对两个链表进行逐位相加，
 *将结果正序存入C链表
 */
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

typedef struct LNode
{   /* 定义结构体函数名称为LNode，指针为LinkList */
    int data;
    struct LNode *next;
}LNode, *LinkList;

LinkList InitList_L(LinkList L)
{   /* 链表初始化，设置空链表以及表头 */
    L = (LinkList)malloc(sizeof(LNode));
    if (!L)
        exit(0);
    L->next = NULL;
    return L;
}

void ListInsert_L(LinkList L, int e)
{   /* 链表头插入 */
    LinkList s;
    s = (LinkList)malloc(sizeof(LNode));
    s->data = e;
    s->next = L->next;
    L->next = s;
}

void DigitInsert(LinkList L, int num)
{   /* 递归将数按位逆序插入链表 */
    if (num > 9)
        DigitInsert(L, num / 10);
    ListInsert_L(L, num % 10);   
}

void ShowList(LinkList L)
{   /* 遍历链表以及打印，从头指针下一个结点开始 */
    LinkList p = L->next;
    while (p!=NULL)
    {
        printf(" %d->", p->data);
        p = p->next;
    }
    printf(" NULL\n");
}

void SumList(LinkList La, LinkList Lb, LinkList Lc)
{   /* A、B链表按位相加，逐位插入C链表 */
    int c = 0;
    LinkList pa = La->next;
    LinkList pb = Lb->next;
    while (pa && pb)    // 当AB链表当前结点都不为空时
    {
        if ((pa->data + pb->data + c) > 9)
            {
                ListInsert_L(Lc, (pa->data + pb->data + c) % 10);
                c = 1;
            }
        else if ((pa->data + pb->data + c) <= 9)
            {
                ListInsert_L(Lc, pa->data + pb->data + c);
                c = 0;
            }
        pa = pa->next;
        pb = pb->next;
    }
    if ((!pa) && (!pb))     // 当AB链表同时结束时
    {   
        if (c)
        {
            ListInsert_L(Lc, c);
            c = 0;
        }   
    }
    if (pa && (!pb))    // 当B链表结束而A链表未结束时
    {
        while (pa)
        {
            if ((pa->data + c) > 9)
            {
                ListInsert_L(Lc, (pa->data + c) % 10);
                c = 1;
            }
            else if ((pa->data + c) <= 9)
            {
                ListInsert_L(Lc, pa->data + c);
                c = 0;
            }
            pa = pa->next;
        }
    }
    if ((!pa) && pb)    // 当A链表结束而B链表未结束时
    {
        while (pb)
        {
            if ((pb->data + c) > 9)
            {
                ListInsert_L(Lc, (pb->data + c) % 10);
                c = 1;
            }
            else if ((pb->data + c) <= 9)
            {
                ListInsert_L(Lc, pb->data + c);
                c = 0;
            }
            pb = pb->next;
        }
    }
}

void DestroyList(LinkList L)
{   /* 销毁链表，将链表头指针置空 */
    LinkList p;
    while (L->next)
    {
        p = L->next;
        L->next = p->next;
        free(p);
    }
    free(L);
    L = NULL;
    p = NULL;
}

int main(void)
{
    LinkList La, Lb, Lc;
    int a, b, e;
    La = NULL;
    Lb = NULL;
    Lc = NULL;

    La = InitList_L(La);
    Lb = InitList_L(Lb);
    Lc = InitList_L(Lc);
    printf("输入A链表插入的数: ");
    scanf("%d", &e);
    a = e;
    DigitInsert(La, e);
    // printf("插入成功\n");

    printf("输入B链表插入的数: ");
    scanf("%d", &e);
    b = e;
    DigitInsert(Lb, e);
    printf("两数和为: %d\n", a + b);
    // printf("插入成功\n");
    printf("---------------------------------\n");
    printf("A链表：\n");
    ShowList(La);
    printf("B链表：\n");
    ShowList(Lb);
    SumList(La, Lb, Lc);
    printf("C链表：\n");
    ShowList(Lc);
    DestroyList(La);
    DestroyList(Lb);

    return 0;
}
