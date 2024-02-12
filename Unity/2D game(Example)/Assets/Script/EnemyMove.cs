using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyMove : MonoBehaviour
{
    public int nextMove = -1;
    Rigidbody2D rigid;
    Animator anim;
    SpriteRenderer spriteRenderer;

    // Start is called before the first frame update
    void Awake()
    {
        rigid = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        spriteRenderer = GetComponent<SpriteRenderer>();
        Invoke("Think", 3);
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        //Move
        rigid.velocity = new Vector2(nextMove, rigid.velocity.y);

        //Check Platform
        Vector2 frontVec = new Vector2(rigid.position.x + nextMove*0.2f, rigid.position.y);
        Debug.DrawRay(frontVec, Vector3.down, new Color(0, 1, 0));
        RaycastHit2D rayHit = Physics2D.Raycast(frontVec, Vector3.down, 1, LayerMask.GetMask("Platform"));
        if (rayHit.collider == null)
            if (rayHit.distance < 0.5f) 
                Turn();
    }

    void Think() {
        //Sprite Animation
        anim.SetInteger("walkSpeed", nextMove);

        //Filp Sprite
        if(nextMove != 0)
            spriteRenderer.flipX = nextMove == 1;

        //Set Next Active
        nextMove = Random.Range(-1, 2);

        float nextThinkTime = Random.Range(2f, 4f);
        Invoke("Think", nextThinkTime);
    }

    void Turn() {
        nextMove *= -1;
        spriteRenderer.flipX = nextMove == 1;

        CancelInvoke();
        Invoke("Think", 5);
    }
}
