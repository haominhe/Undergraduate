using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class colliderer : MonoBehaviour {
	public Transform[] SpawnPoints;
	public GameObject[] player;

	void OnParticleCollision(GameObject other) {
		if (other.tag == "player1") {
			other.transform.position = SpawnPoints[0].position; 

		}
		if (other.tag == "player2") {
			other.transform.position = SpawnPoints[1].position; 
		}
	}
}
