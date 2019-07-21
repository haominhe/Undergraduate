using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ButtonManager : MonoBehaviour {

	private GameObject StartImage;
	//public GameObject gameManager;          //GameManager prefab to instantiate.

	public void NewGameBtn(string newGameLevel){
		StartImage = GameObject.Find("GameStart");
		Destroy(StartImage);
		StartImage.SetActive (false);
		//GameManager.instance.InitGame();
	}

	public void ExitGameBtn(){
		Application.Quit ();
	}

	//public void RetryGameBtn(){
	//	if (GameManager.instance == null)

			//Instantiate gameManager prefab
	//		Instantiate(gameManager);
	//}
}
