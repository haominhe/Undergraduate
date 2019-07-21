using UnityEngine;
using System.Collections;

public class WarriorAnimationDemoFREE : MonoBehaviour 
{
	private Animator animator;

	float rotationSpeed = 30;

	Vector3 inputVec;
	Vector3 targetDirection;
	
	//Warrior types
	public enum Warrior{Karate, Ninja, Brute, Sorceress, Knight, Mage, Archer, TwoHanded, Swordsman, Spearman, Hammer, Crossbow};
    public string horizontal_input;
    public string vertical_input;
    public string attack_input;
    public string attack_trigger;
    public Warrior warrior;
    private float z;
    private float x;
    private float att;
    public Collider hitbox;
    
    Animator enemy_anim;
    //private float speed = 1;

    void Start(){
    	animator = GetComponent<Animator>();

    }
	
	void Update()
	{
		//Get input from controls
		z = Input.GetAxisRaw(horizontal_input);
		x = -(Input.GetAxisRaw(vertical_input));
		//att = Input.GetAxisRaw()
		inputVec = new Vector3(x, 0.0f, z);

		//Apply inputs to animator
		animator.SetFloat("Input X", z);
		animator.SetFloat("Input Z", -(x));
        
        //disable the attack hit box collider
		hitbox.enabled = false;

		if (x != 0 || z != 0 )  //if there is some input
		{
			//set that character is moving
			animator.SetBool("Moving", true);
			animator.SetBool("Running", true);
		}
		else
		{
			//character is not moving
			animator.SetBool("Moving", false);
			animator.SetBool("Running", false);
		}
		if (animator.GetInteger("HaveFood") > 0)
        {
            animator.speed = 0.7f;
        }
        else
        {
            animator.speed = 1.0f;
        }

        if (animator.GetBool("HaveBomb"))
        {
            animator.speed = 0.8f;
        }
        else
        {
            animator.speed = 1.0f;
        }

        if (Input.GetButtonDown(attack_input))
		{
			animator.SetTrigger(attack_trigger);
			if (warrior == Warrior.Brute)
				StartCoroutine (COStunPause(1.2f));

			else if (warrior == Warrior.Sorceress)
				StartCoroutine (COStunPause(1.2f));
			else
				StartCoroutine (COStunPause(.6f));
			launch_attack(hitbox);
		}

		if(animator.GetBool("Gethit")){
			StartCoroutine(stuntime());
			Debug.Log(this.gameObject.name + " got hit");
			animator.enabled=false;
			this.gameObject.GetComponent<Rigidbody>().constraints = RigidbodyConstraints.FreezePositionX | RigidbodyConstraints.FreezePositionY | RigidbodyConstraints.FreezePositionZ
			| RigidbodyConstraints.FreezeRotationX | RigidbodyConstraints.FreezeRotationY | RigidbodyConstraints.FreezeRotationZ;
			animator.SetBool("Gethit", false);			
			//this.gameObject.SetActive(true);
			//animator.enabled=true;
			



		}

        UpdateMovement();  //update character position and facing
	}

	IEnumerator stuntime(){
		yield return new WaitForSeconds(1);
		//this.gameObject.SetActive(true);
		this.gameObject.GetComponent<Rigidbody>().constraints =  RigidbodyConstraints.FreezePositionY | RigidbodyConstraints.FreezeRotationX | RigidbodyConstraints.FreezeRotationY 
		| RigidbodyConstraints.FreezeRotationZ;
		animator.enabled=true;
		Debug.Log("waited 1 seconds");
	}

	public IEnumerator COStunPause(float pauseTime)
	{
		yield return new WaitForSeconds(pauseTime);
	}

	//converts control input vectors into camera facing vectors
	void TargetDirectionUpdate()
	{  
		

		// Target direction update
		targetDirection = -(inputVec) ;
	}

	//face character along input direction
	void RotateTowardMovementDirection()  
	{
		if (inputVec != Vector3.zero)
		{
			transform.rotation = Quaternion.Slerp(transform.rotation, Quaternion.LookRotation(targetDirection), Time.deltaTime * rotationSpeed);
		}
	}

	void UpdateMovement()
	{
		//get movement input from controls
		Vector3 motion = inputVec;

		//reduce input for diagonal movement
		motion *= (Mathf.Abs(inputVec.x) == 1 && Mathf.Abs(inputVec.z) == 1) ? 0.7f:1;

		RotateTowardMovementDirection();  
		TargetDirectionUpdate();  
	}


	private void launch_attack(Collider col){
		col.enabled = true;
		var cols = Physics.OverlapBox(col.bounds.center, col.bounds.extents, col.transform.rotation, LayerMask.GetMask("Players"));
		foreach(Collider c in cols){
			if(c.gameObject.CompareTag(this.gameObject.tag))
				continue;
			Debug.Log(c.gameObject.name);
			enemy_anim = c.gameObject.GetComponent<Animator>();
			enemy_anim.SetBool("Gethit", true);
		}
			
		col.enabled = false;
	}
}