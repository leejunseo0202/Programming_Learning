using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerBall : MonoBehaviour { 
    public float jumpPower;
    public int score = 0;
    public GameManagerLogic manager;
    public float speed;
    int isJump = 0;


    AudioSource audioSourse;
    Rigidbody rigid;
    private void Awake() {
        audioSourse = GetComponent<AudioSource>();
        rigid = GetComponent<Rigidbody>();
    }

    private void Update()
    {
        if (Input.GetButtonDown("Jump") && isJump <= 1)
        {
            isJump++;
            rigid.AddForce(new Vector3(0, jumpPower, 0), ForceMode.Impulse);
        }
    }
    void FixedUpdate() { 
        float horizontal = Input.GetAxisRaw("Horizontal");
        float vertical = Input.GetAxisRaw("Vertical");
        Vector3 vector = new Vector3(horizontal, 0, vertical);

        rigid.AddForce(vector / 100 * speed, ForceMode.Impulse);
    }

    void OnCollisionEnter(Collision collision) { 
        if (collision.gameObject.tag == "Floor")
            isJump = 0;
    }

    void OnTriggerEnter(Collider other) { 
        if (other.tag == "Item") { 
            score++;
            audioSourse.Play();
            other.gameObject.SetActive(false);
            manager.GetItem(score);
        }
        else if (other.tag == "Goal") {
            if (score == manager.totalItemCount) {
                SceneManager.LoadScene(manager.stage+1);
            }
            else {
                SceneManager.LoadScene(manager.stage);
            }
        }
    }
}
